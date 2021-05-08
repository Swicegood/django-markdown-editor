//import React, { Component } from 'react';
//import ReactDOM from 'react-dom';
//import Axios from 'axios';
//import { Container, Row, Table, Col, Collapse, Button } from 'react-bootstrap';
// import TableRow from "{% static 'face_website/js/TableRow.js' %}";

class TestsTable extends React.Component {
    constructor(props) {
        super(props)
        
        this.state = {
            page: 1,
            lastPage: 1,
            data: [],
            showTable: false,
            refresh: true,
            interval: null
        }
    }

    componentDidMount() {
        this.getData();
        var int = setInterval(this.getData, 10000);
        this.setState({
            interval: int
        });
    }

    componentWillUnmount() {
        clearInterval(this.state.interval);
    }

    getData = (page = this.state.page, refresh = true) =>{
        $.ajax({
            context: this,
            type: 'GET',
            url: '../data-json/0',
            success: function(response){
            var fulldata = JSON.parse(response.data)
            var lastPage = fulldata.length/10 + 1 
            this.setState({
                lastPage: lastPage
            })
            }
        }),    
        $.ajax({
            context: this,
            type: 'GET',
            url: '../data-json/'+page*10,
            success: function(response){
            var data = JSON.parse(response.data)
           
            if(!refresh) {
                data = this.state.data.concat(data);         
            }                           

            this.setState({
                data: data,
                page: page,
                refresh: refresh
            })
            }   
        })
        
        
        .catch((err) => {
            console.log(err);
        
        })
    }

    getMoreData = () => {
        var page = this.state.page;
        page = page + 1;

        if(this.state.refresh) {
            clearInterval(this.state.interval);
        }

        this.getData(page, false);
    }

    toggleCollapse = () => {
        var show = this.state.showTable;

        if(show) {
            this.setState({
                showTable: false
            });
        } else {
            this.setState({
                showTable: true
            });
        }
    }

    render() {
        var page = this.state.page;
        var lastPage = this.state.lastPage;
        var data = this.state.data;
        var show = this.state.showTable;
        var refresh = this.state.refresh;
        if(data.length > 0) {
            return (
                <div>
                    <window.ReactBootstrap.Container className="mb-4 mt-4 px-5 bg-dark text-light" fluid="True">
                        <window.ReactBootstrap.Row>
                            <window.ReactBootstrap.Col sm={{ span: 12 }} className="mb-3 text-center">
                                <div>
                                    <h4 className="d-inline mr-2">All tests</h4>
                                    <span className="text-muted">Auto refresh: {(refresh) ? 'On' : 'Off'}</span>
                                </div>
                            </window.ReactBootstrap.Col>
                        </window.ReactBootstrap.Row>
                        <window.ReactBootstrap.Row >
                            <window.ReactBootstrap.Col sm={{ span: 12 }} id="testsTable" className="text-light">
                                <window.ReactBootstrap.Table responsive className="text-light text-start">
                                    <thead>
                                        <tr>
                                            <th>ID</th>
                                            <th>Date</th>
                                            <th>Arotik</th>
                                            <th>Face</th>
                                            <th>More</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {data.map((e,i) => {
                                            return (
                                                <TableRow key={e.pk} data={e} />
                                            );
                                        })}
                                    </tbody>
                                </window.ReactBootstrap.Table>
                            </window.ReactBootstrap.Col>
                        </window.ReactBootstrap.Row>
                        {page < lastPage &&
                            <window.ReactBootstrap.Row>
                                <window.ReactBootstrap.Col sm={{ span: 12 }} className="text-center">
                                    <window.ReactBootstrap.Button variant="primary" onClick={this.getMoreData}>Show more</window.ReactBootstrap.Button>
                                </window.ReactBootstrap.Col>
                            </window.ReactBootstrap.Row>
                        }
                    </window.ReactBootstrap.Container>
                </div>
            );
        } else {
            return (
                <>
                </>
            )
        }
    }
}

if (document.getElementById('TestsTable')) {
    ReactDOM.render(<TestsTable />, document.getElementById('TestsTable'), console.log('rendered'));
}
