import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import styles from '../styles/Home.module.css'
import { useEffect, useState } from 'react'
import firebaseConfig from '../config/firebase.config'
import { getDatabase, get, ref, child } from 'firebase/database'
import { initializeApp } from 'firebase/app'
import { getAnalytics } from 'firebase/analytics'
import Event, { EventType } from '../components/Event'

export default function Home() {
  const app = initializeApp(firebaseConfig)
  //const analytics = getAnalytics(app)
  const dbRef = ref(getDatabase());
  const [description, setDescription] = useState<string>('');
  const [events, setEvents] = useState<EventType[] | undefined>();
  useEffect(() => {
    get(child(dbRef, '/description')).then((snapshot) => {
      if (snapshot.exists()) {
        setDescription(snapshot.val())
      } else {
        console.log("No data")
      }
    }).catch((error) => {
      console.error(error)
    })
  }, []);
  useEffect(() => {
    get(child(dbRef, '/events')).then((snapshot) => {
      if (snapshot.exists()) {
        setEvents(snapshot.val())
      } else {
        console.log("No data")
      }
    }).catch((error) => {
      console.error(error)
    })
  }, []);
  return (
    <>
      <Head>
        <title>toros</title>
        <meta name="description" content="experimental music duo" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="" />
      </Head>
     <div className={styles.bgWrap}>
      <Image
        alt="Toros"
        src="/toros.jpg"
        quality={100}
        fill
        sizes="100vw"
        style={{
          objectFit: 'cover',
        }}
      />
    </div>
    <main className={styles.main}>

       <h1>toros</h1>
        <div className={styles.center}>
         <p>{description ? description : "Loading..."}</p>
        </div>
        
       <div className={styles.grid}>
        { events 
        ? 
          <div> 
          <h2>Past Events</h2>
          <table className={styles.card}>
            <thead>
              <tr>
                <td>Title</td>
                <td>Institution</td>
                <td>Date</td>
                <td>Employer</td>
                <td>Location</td>
                <td>Url</td>
              </tr>
            </thead>
            <tbody>
              {events.map((event: EventType, index: number) =>
               <tr key={`${index}-${event.title}`}>
                <td>{event.title}</td>
                <td>{event.institution}</td>
                <td>{event.date.toString()}</td>
                <td>{event.employer}</td>
                <td>{event.location}</td>
                <td>{event.url?<Link href={event.url}>{event.url}</Link>:null}</td>
               </tr>
              ).reverse()}
            </tbody>
          </table>
          </div>
        : 
          "Loading..." }
       </div>
     </main> 
  </>
  )
}
