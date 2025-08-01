import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import ElectionMain from './pages/ElectionMain'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <Header /> */}
      <ElectionMain />
      {/* <StickyHeadTable/> */}
    </>
  )
}

export default App
