import React from 'react'
import {BrowserRouter as Router, Routes,Route, Navigate} from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import Notfound from './pages/Notfound'
import ProtectedRoutes from './components/ProtectedRoutes'


function Logout() {
  localStorage.clear()
  return  <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return  <Register/>
}

const App = () => {
  return (
   <Router>
       <Routes >
        <Route path='/' element={<ProtectedRoutes><Home/></ProtectedRoutes>} />
        <Route path='/login' element={<Login/>} />
        <Route path='/register' element={<Register/>} />
        <Route path='/logout' element={<Logout/>} />
        <Route path='*' element={<Notfound/>} />
       </Routes>
   </Router>
  )
}

export default App