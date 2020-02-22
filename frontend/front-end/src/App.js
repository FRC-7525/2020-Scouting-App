import React, { Component } from 'react';
import './App.css';

import Navbar from "./components/nav/navbar";
import ApplicationViews from "./components/applicationViews";

class App extends Component {

	state = {
		loggedIn: false,
		token: "",
		api: "http://localhost:8000"
	}

	logIn = function (res) {
		this.setState({ token: `token ${res.token}`, loggedIn: true })

	}.bind(this)

	logOut = function () { 
		this.setState({ token: "", loggedIn: false })
	}.bind(this)

	previousLoggedIn = function(){
		if(localStorage.getItem('scoutingAuth') !== null){
			let auth = localStorage.getItem('scoutingAuth')
			let res = {
				token: auth
			}
			this.logIn(res)
		}
	}.bind(this)

	componentDidMount(){
		let root = document.getElementById('root')
		root.classList.add('hero')
		this.previousLoggedIn()
		
	}

	render() {
		return (
			<React.Fragment>
				<Navbar loggedIn={this.state.loggedIn} api={this.state.api} />
				<ApplicationViews loggedIn={this.state.loggedIn} logIn={this.logIn} logOut={this.logOut} api={this.state.api} token={this.state.token} />
			</React.Fragment>
		)
	}
}

export default App;
