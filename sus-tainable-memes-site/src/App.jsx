import { useState } from 'react'
import './App.css'
import Header from "./components/Header"
import TextInput from './components/TextInput'
import logo from "../public/favicon.png"

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <img src={logo} className='site-logo'/>
      <Header />
      <p>Imagine a sustainable meme...</p>
      <TextInput />
      
    </div>
  )
}

export default App
