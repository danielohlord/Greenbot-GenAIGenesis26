import { useState } from "react"
import "./TextInput.css"

function TextInput(){
    // Update text variable with setText and useState
    const [text, setText] = useState("")


    function handleSubmit(e){ // e is the event obj
        e.preventDefault() // Dont refresh page
        console.log(text) // Debug thingy to check proper input
        setText("")
    }

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Generate a sus-tainable meme text..."
                value={text}
                onChange={(e) => setText(e.target.value)}
                />
            <button type="submit">
                Generate!
            </button>
        </form>
    )
}

export default TextInput