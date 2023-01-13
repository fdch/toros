import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import styles from '../styles/Home.module.css'
import Grid from '@mui/material/Grid'
import { useEffect, useState } from 'react'
import firebaseConfig from '../config/firebase.config'
import { getDatabase, get, ref, child } from 'firebase/database'
import { initializeApp } from 'firebase/app'
import { getAnalytics } from 'firebase/analytics'
import Event, { EventType } from '../components/Event'

type Member = {
  name: string
  url: string
}

export default function Home() {
  const app = initializeApp(firebaseConfig)
  useEffect( () => {
    const analytics = getAnalytics(app)
  }, [app])
  const dbRef = ref(getDatabase());
  const [description, setDescription] = useState<string>('');
  const [members, setMembers] = useState<Member[] | undefined>();
  const [eventsPast, setEventsPast] = useState<EventType[] | undefined>();
  const [eventsNext, setEventsNext] = useState<EventType[] | undefined>();

  useEffect(() => {
    get(child(dbRef, '/members')).then((snapshot) => {
      if (snapshot.exists()) {
        setMembers(snapshot.val())
      } else {
        console.log("No data")
      }
    }).catch((error) => {
      console.error(error)
    })
  }, []);


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

  const setEvents = (events: EventType[]) => {
    const today = new Date
    setEventsNext(events.filter((e:EventType) => new Date(e.date) > today))
    setEventsPast(events.filter((e:EventType) => new Date(e.date) <= today))
  }

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
        <meta name="description" content={description} />
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
       <h2>an experimental music duo</h2>

        <div className={styles.center}>
          { description
          ?
           <p>{description}</p>
          :
           <p>Loading description ...</p>
          }
        </div>

        { eventsNext 
        ? eventsNext.length == 0 ? null :
          <>
          <h2>Next Events</h2>
          <div className={styles.grid}>
              {eventsNext.map((event: EventType,index: number) =>
               <Event key={`${index}-${event.title}`} event={event}/>
              ).reverse()}
          </div>
          </>
        : 
          <p>Loading next events...</p>
        }

        { eventsPast  
        ? eventsPast.length == 0 ? null :
          <>
          <h2>Past Events</h2>
          <div className={styles.grid}>
              {eventsPast.map((event: EventType,index: number) =>
               <Event key={`${index}-${event.title}`} event={event}/>
              ).reverse()}
          </div>
          </>
        : 
          <p>Loading past events...</p>
        }
        
        { members
        ? 
         <>
         <h2>About Us</h2>
         <div className={styles.grid}>
          {members.map((member: Member) => 
            <>
              <h3>{member.name}</h3>
              <Link href={member.url}>{member.url}</Link>
            </>
          )}
         </div>
         </>
        : 
          <p>Loading members... </p>
        }

     </main> 
  </>
  )
}
