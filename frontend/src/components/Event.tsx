import styles from '../styles/Home.module.css'
import Link from 'next/link'
import Image from 'next/image'
import Typography from '@mui/material/Typography'
import Card from '@mui/material/Card'
import Grid from '@mui/material/Grid'
import CardActions from '@mui/material/CardActions'
import CardMedia from '@mui/material/CardMedia'
import CardContent from '@mui/material/CardContent'
import { styled } from '@mui/material/styles';


const Item = styled(Card)(({ theme }) => ({
  ...theme.typography.body2,
  padding: theme.spacing(0.2),
  backgroundColor: "rgba(0,0,0,0.2)",
  color: "rgba(255,255,255,1)",
  elevation: 10,
  textAlign: 'center',
}));


export type EventType = {
  url: string
  institution: string
  location: string
  title: string
  employer: string
  date: Date
  images: string[]
  audio: string[]
  videos: string[]

}

export default function Event(
  { event } : { event: EventType }
) {
  const sliceURL = (url: string) => url.length>=30?url.slice(0,30)+"...":url
  
  const date = new Date(event.date)

  return (
    <Item sx={{margin:1.5}}>

      <CardContent>

        <Grid container spacing={2}>
          <Grid item>
          <Typography sx={{ fontSize: 13 }}>
          {event.location}
          </Typography>
          </Grid>
          <Grid item>
          <Typography sx={{ fontSize: 13 }}>
            {date.toDateString()}
          </Typography>
          </Grid>
          <Grid item>
          <Typography sx={{ fontSize: 13 }}>
            {date.toLocaleTimeString()}
          </Typography>
          </Grid>
        </Grid>
        
        <Typography variant="h5" component="div">
         {event.title}
        </Typography>

        { !event.employer ? null :
          <Typography>
           {event.employer}
          </Typography>
        }
          <Typography sx={{ fontSize: 13 }}>
            {event.institution}
          </Typography>
             
      
      <Grid container>
      { !event.url ? null :
       <Grid item>
        <Link href={event.url}>
        {
        `(web) ${sliceURL(event.url)}`
        }
        </Link>
       </Grid>
      }
      </Grid>
      <Grid container>
      { !event.videos ? null :
       <Grid item>

        {
          event.videos.map((url: string, index:number) =>
            <Link key={url} href={url}>
              {
              `(video) ${sliceURL(url)}`
              }
            </Link>
           )  
        }
       </Grid>
      }
      </Grid>
      </CardContent>
    </Item>
  )
}
