# GreenBot AI

A website that generates AI memes to educate the masses on sustainability and sustainable practices.

---

## Table of Contents

- [Installation](#installation)
- [Hosting](#hosting-locally)

---

## Installation

** Node.js is required to be installed already.
- [Install Node.js Here](https://nodejs.org/)

1. Confirm you have installed node.js properly:

```
node -v
npm -v
```

Which should return version numbers. If an error comes up then refer to [here](https://nodejs.org/) for troubleshooting. Now use ```cd``` to navigate to where you want to clone the repository.

2. Clone the repository:

```
git clone https://github.com/danielohlord/Greenbot-GenAIGenesis26.git
```
3. API Setup:

There should be a pre-existing .env file in the root of the repository, get a Gemini API key with access to:

- gemini-3.1-flash-image-preview
- gemini-3.0-flash-preview

Both of which do cost some balance in your Gemini API account.

The .env file should look like:
```
GEMINI_API_KEY=your_api_key
```
Replace ```your_api_key``` with an actual API key, no punctuation.

4. Go into your local copy with ```cd [local_copy_name]``` and run the following to install back-end dependencies:

```
pip install -r requirements.txt
```
5. Go into website folder:

```
cd sus-tainable-memes-site
```

6. Install front-end dependencies:
```
npm install
```

Follow the installation instructions in console, and when prompted, pick Vite.

## Hosting Locally

Start React Development Server And Run Python

```bash
npm run dev
python app.py
```
