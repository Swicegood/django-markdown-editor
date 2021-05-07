//import React, { Component } from 'react';
//import ReactDOM from 'react-dom';
//import { Modal, Button } from 'react-bootstrap';
//import Axios from 'axios';
//import { toast } from 'react-toastify';

class TableRow extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            data: this.props.data,
            show: false,
        }
    }

    toggleShow = () => {
        var show = this.state.show;
        if(show) {
            this.setState({
                show: false
            });
        } else {
            this.setState({
                show: true
            });
        }
    }

    delete = (id) => {
        var url = 'api/speedtest/delete/' + id;

        Axios.delete(url)
        .then((resp) => {
            console.log(resp);
            toast.success('Speedtest deleted');
        })
        .catch((err) => {
            if(err.response.status == 404) {
                toast.warning('Speedtest not found');
            } else {
                toast.error('Something went wrong');
            }
        })

        this.toggleShow();
    }

    render() {
        var e = this.state.data;
        var show = this.state.show;
        try{
            if (e.fields.upload != null){
            var imgsrc = "../media/"+e.fields.upload
            }
        }
        catch(err){
            {}
        }

        if(e.failed != true) {
            return (
                <tr>
                    <td>{e.pk}</td>
                    <td>{e.fields.date}</td>
                    <td>{e.fields.arotik}</td>
                    <td>{e.fields.face}</td>
                    {e.fields.upload != null ?
                     
                        <td>
                            <span onClick={this.toggleShow} className="bi-arrow-up-right"></span>
                            <window.ReactBootstrap.Modal show={show} onHide={this.toggleShow} dialogClassName="border-radius-2">
                                <window.ReactBootstrap.Modal.Header closeButton>
                                    <window.ReactBootstrap.Modal.Title className="text-light">Screenshot</window.ReactBootstrap.Modal.Title>
                                </window.ReactBootstrap.Modal.Header>
                                <window.ReactBootstrap.Modal.Body className="text-center">      
                                     <img src={imgsrc} height='200px'></img>                         
                                    
                                </window.ReactBootstrap.Modal.Body>
                            </window.ReactBootstrap.Modal>
                        </td>
                    :
                        <td></td>
                    }
                </tr>
            );
        } else {
            return (
                <tr>
                    <td>{e.id}</td>
                    <td>{new Date(e.created_at).toLocaleString()}</td>
                    <td><span className="ti-close text-danger"></span></td>
                    <td><span className="ti-close text-danger"></span></td>
                    <td><span className="ti-close text-danger"></span></td>
                    <td></td>
                </tr>
            );
        }
    }
}

if (document.getElementById('tableRow')) {
    ReactDOM.render(<TableRow />, document.getElementById('tableRow'));
}