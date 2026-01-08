import './App.css'
import LogButton from './components/LogButton'
import { useState } from 'react'

function App() {
  const [username, setUsername] = useState('');
  return (
    <div className="h-screen flex flex-col items-center justify-center gap-4">
      <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} className="border border-gray-300 rounded px-2 py-1 mr-2" />
      <div className="flex flex-row gap-2">
        <LogButton severity="info" title="[INFO] Message" username={username} />
        <LogButton severity="warning" title="[WARNING] Message" username={username} />
        <LogButton severity="error" title="[ERROR] Message" username={username} />
      </div>
    </div>
  )
}

export default App
