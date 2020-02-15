import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getRecents } from "../../../actions/lists";

import { ListGroup, ListGroupItem } from "reactstrap";

const placeholderList = [1, 2, 3, 4, 5]

export class Recents extends Component {
    static propTypes = {
        recents: PropTypes.array
    };
    componentDidMount() {
        this.props.getRecents();
    }
    render() {
        return (
            <>
                <ListGroup className="text-center">
                    {this.props.recents ?
                        this.props.recents.map((system, index) => (
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
                        ))
                        : placeholderList.map(index => (
                            <ListGroupItem
                                tag="a"
                                href=""
                                className="py-2"
                                action
                                disabled
                                key={index}>

                            </ListGroupItem>
                        ))
                    }
                </ListGroup>
                <div className="text-center">
                    <small className="text-muted mt-2">Recents</small>
                </div>
            </>
        );
    }
}

const mapStateToProps = state => ({
    recents: state.recents.recents
});

export default connect(mapStateToProps, { getRecents })(Recents);
