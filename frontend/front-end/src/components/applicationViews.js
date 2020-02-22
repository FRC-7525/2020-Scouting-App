import { Route } from 'react-router-dom'
import React, { Component } from "react"
import Login from "./login/login"
import Home from "./home/home"
import Register from "./register/register"
import Logout from './login/logout'



export default class ApplicationViews extends Component {

    state = {
        
    }

    render() {
        return (
            <React.Fragment>
                <Route exact path="/" render={(props) => {
                    return <Home {...props} loggedIn={this.props.loggedIn}/>
                }} />
                <Route exact path="/login" render={(props) => {
					return <Login {...props} logIn={this.props.logIn} api={this.props.api}/>
                }} />
                <Route exact path="/logout" render={(props) => {
					return <Logout {...props} logOut={this.props.logOut} api={this.props.api}/>
                }} />
				<Route exact path="/register" render={(props) => {
					return <Register {...props} logIn={this.props.logIn} api={this.props.api}/>
				}} />
				{/* <Route exact path="/listen/:id" render={(props) => {
					return <Player {...props} api={this.props.api} token={this.props.token} loggedIn={this.props.loggedIn} isBand={this.props.isBand}/>
				}} />
				<Route exact path="/listen/genre/:id" render={(props) => {
					return <Player {...props} api={this.props.api} token={this.props.token} loggedIn={this.props.loggedIn} isBand={this.props.isBand}/>
				}} /> */}
            </React.Fragment>
        )
    }
}