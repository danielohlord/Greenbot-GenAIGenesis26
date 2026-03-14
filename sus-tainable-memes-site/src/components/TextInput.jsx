import { useState } from "react"
import "./TextInput.css"

function TextInput(){
    // Update text variable with setText and useState
    const [text, setText] = useState("")
    const [image, setImage] = useState(null) // store submitted image
    const [loading, setLoading] = useState(false) // Get the image loading state


    async function handleSubmit(e){ // e is the event obj
        e.preventDefault() // Dont refresh page
        console.log(text) // Debug thingy to check proper input
        setText("")
        setLoading(true) // show loading message to user

        try {
            // Send input to Python
            await fetch("http://localhost:5000/generate", {
                method: "POST",
                headers: {"Content-type": "application/json"},
                body: JSON.stringify({text}),
            })

            // Keep checking if the image we need exists
            const checkImage = async() => {
                let exists = false;
                while(!exists){
                    try {
                        // Try getting it
                        const res = await fetch("http://localhost:5000/generated_image.png", { method: "HEAD" })
                        if (res.ok) exists = true
                        else await new Promise(r => setTimeout(r, 1000)) // Try every second
                    } catch (err) {
                        await new Promise(r => setTimeout(r, 1000))
                    }
                }
            }

            await checkImage()
            setImage("http://localhost:5000/generated_image.png")
        }catch (err){
            console.error(err)
        }finally{
            setLoading(false)
        }
    }

    return (
        <div className="text-input-container">
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Enter meme text..."
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                />
                <button type="submit">Submit</button>
            </form>

            {loading && <p>Generating Image...</p>}
        
            {image && (
                <div className="image-display">
                    <img src={image} alt="Generating" />
                </div>
            )}
        </div>
    )
}

export default TextInput