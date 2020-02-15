import React, { Component } from "react";

import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getPopular } from "../../../actions/lists";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEdit } from "@fortawesome/free-solid-svg-icons";

import { ListGroup, ListGroupItem } from "reactstrap";

const placeholderList = [1, 2, 3, 4, 5]

export class Popular extends Component {
    static propTypes = {
        popular: PropTypes.array
    };
    componentDidMount() {
        this.props.getPopular();
    }
    render() {
        return (
            <>
                <ListGroup className="text-center">
                    {this.props.popular ?
                        this.props.popular.map((system, index) => (
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
                <div className="d-flex justify-content-around">
                    <div className="invisible"><FontAwesomeIcon icon={faEdit} size="sm" className="text-info" /></div>
                    <div><small className="text-muted">Popular</small></div>
                    <div><FontAwesomeIcon icon={faEdit} size="sm" className="text-info" /></div>
                </div>
            </>
        );
    }
}

const mapStateToProps = state => ({
    popular: state.popular.popular
});

export default connect(mapStateToProps, { getPopular })(Popular);
