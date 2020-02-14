import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getRecents } from "../../../actions/lists";

import { ListGroup, ListGroupItem } from "reactstrap";

export class Recents extends Component {
    static propTypes = {
        recents: PropTypes.array
    };
    componentDidMount() {
        this.props.getRecents();
    }
    render() {
        console.log(this.props.recents);
        return (
            <>
                <ListGroup className="text-center">
                    {this.props.recents.map((system, index) => (
                        <ListGroupItem
                            tag="a"
                            href=""
                            className="py-2"
                            action
                            disabled={system ? false : true}
                            key={index}
                        >
                            {system ? system : "N/A"}
                        </ListGroupItem>
                    ))}
                    <small className="text-muted mt-2">Recents</small>
                </ListGroup>
            </>
        );
    }
}

const mapStateToProps = state => ({
    recents: state.recents.recents
});

export default connect(mapStateToProps, { getRecents })(Recents);
