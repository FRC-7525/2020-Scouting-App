import React, { Component } from "react"

export default class Home extends Component {

	
	checkAuth = function(){
		if(!this.props.loggedIn){
			return 	<div>
						<div className='level'>
							<p className='level-item title is-5'>Please Log in or register</p>
						</div>
					</div>
		}
	}

	

    render() {
        return (
			<div className='container'>
				<div className='level'>
					<h1 className='level-item title'>Welcome to FRC 7525 Scouting 2020</h1>
				</div>
				{this.checkAuth()}
			</div>
		)
    }
}