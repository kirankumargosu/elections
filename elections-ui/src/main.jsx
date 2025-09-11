import { createRoot } from 'react-dom/client'
import './css/index.css'
import App from './App.jsx'
import { ContextProvider } from "./Context";

createRoot(document.getElementById('root')).render(
  <ContextProvider>
    <App />
  </ContextProvider>,
)
