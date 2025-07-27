import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Tamilnadu from './components/Tamilnadu'
import StickyHeadTable from './components/StickyHeadTable'
import Mast from './components/Mast'
import Legend from './components/Legend'
import Header from './components/Header'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <Header /> */}
      <Mast />
      <Legend />
      <Tamilnadu />
      {/* <StickyHeadTable/> */}
    </>
  )
}

export default App
