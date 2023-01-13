import styles from '../styles/Home.module.css'
import Link from 'next/link'
import Image from 'next/image'
import Typography from '@mui/material/Typography'
import Card from '@mui/material/Card'
import CardActions from '@mui/material/CardActions'
import CardMedia from '@mui/material/CardMedia'
import CardContent from '@mui/material/CardContent'

export type EventType = {
  url: string
  institution: string
  location: string
  title: string
  employer: string
  date: Date
  image: string[]
  audio: string[]
  video: string[]

}

export default function Event(event:EventType) {
  return (
    <Card>
      <CardContent>
      <Typography>
       {event.title}
      </Typography>
      <Typography>
      {event.institution}
      </Typography>
      <Typography>
      {event.date.toString()}
      </Typography>
      <Typography>
      {event.employer}
      </Typography>
      <Typography>
      {event.location}
      </Typography>
      </CardContent>
      <CardMedia>
      {event.url?<Link href={event.url}>{event.url}</Link>:null}
      </CardMedia>
      <CardActions>
      </CardActions>
    </Card>
  )
}
