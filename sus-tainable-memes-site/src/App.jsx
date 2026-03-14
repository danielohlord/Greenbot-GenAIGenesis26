import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Header from "./components/Header"
import TextInput from './components/TextInput'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <Header />
      <p>Imagine a sustainable meme...</p>
      <TextInput />
    </div>
  )
}

export default App
