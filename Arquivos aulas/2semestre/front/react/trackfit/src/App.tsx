import { useState } from 'react'
import {Workoutcard } from './components/workout-card'
import { Header } from './components/header'

function App() {
  const [count, setCount] = useState(0)

  return (

    

    <main>
      <Header/>
    <Workoutcard 
    id='2'
    title="popada"
    date="20/02/2026"
    durationMinutes={60}
    intesity={4}
    />
    
    </main>
  )
}

export default App
