import React, { Component } from "react"
import { Link } from "react-router-dom"
// import '../styles/nav.css'
import "../styles/nav.css"


export default class Navbar extends Component {

	state = { }

	loggedIn = function(){
		if(this.props.loggedIn){
			return 	<div className='level-right'>
						<li>
							<Link className='button is-warning is-inverted' to='/logout'>Logout</Link>
						</li>
					</div>
		}else{
			return <div className='level-right'>
					<li>
						<Link className='button is-warning is-inverted' to="/login">Login</Link>
					</li>
					<li>
						<Link className='button is-warning is-inverted' to="/register">Register</Link>
					</li>
				</div>
		}
	}


    render() {
        return (
            <nav id='nav' className='notification'>
                <ul className='level'>
                    <li className='level-left'>
                        <Link to="/"><h2 className="title is-2">Home</h2></Link>
                    </li>
					{this.loggedIn()}
                </ul>
            </nav>
        )
    }
}