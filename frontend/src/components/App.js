import React , {Component} from "react";
import ReactDOM from "react-dom";

import {
    Navbar,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink
  } from 'reactstrap';

class App extends Component {
    render() {
        return <h1>React App</h1>
        // <div>
        //     <Navbar color="light" light>
        //         <NavbarBrand href="/">Blue Donut</NavbarBrand>
        //         <Nav className="mr-auto" navbar>
        //             <NavItem>
        //                 <NavLink href="/map/region/">Regions</NavLink>
        //             </NavItem>
        //             <NavItem>
        //                 <NavLink href="/map/system/D-PNP9">Systems</NavLink>
        //             </NavItem>
        //         </Nav>
        //     </Navbar>
        // </div>
    }
}

ReactDOM.render(<App />, document.getElementById('app'))