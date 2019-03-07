import React, { Component } from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'
import {Button, Form, Header} from 'semantic-ui-react'
import {Redirect} from "react-router";
import axios from "axios";

class RegistrationForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            email: "",
            password: '',
            errorEmail:false,
            errorPassword:false,
            loading:false,
        }
    }

    componentDidMount() {

    }
    changeEmail=(e)=>{
        this.setState({email:e.target.value})
        this.setState({errorEmail: false})
    }
    changePassword=(e)=>{
        this.setState({password:e.target.value})
        this.setState({errorPassword: false})
    }
    register=()=> {
        let { email, password} = this.state;
        if (!email || !password) {
            if (!email) {
                this.setState({errorEmail: true})
            }
            if (!password) {
                this.setState({errorPassword: true})
            }
        } else {
            this.setState({loading: true})
            let data={
                email:email,
                password:password,
            }
            localStorage.setItem('jwtToken', JSON.stringify(data));
            this.props.dispatch({type: 'addUserProfile', data: data});
            this.props.dispatch({type: 'activeMenuItem', data: "Dashboard"});

            /*axios.post('/login',{data:data}).then(
                function (response, err) {
                    console.log(response)
                    if(response.data){
                        this.setState({loading:false})
                    }
                }.bind(this)
            );*/
        }
    }
    render() {
        if(this.props.userProfile){
            return (<Redirect to={'/dashboard'}/>);
        }else {
            return (<div className='registrationForm-Container'>
                <div className="registrationForm-Container-upper-container">
                    <div className="registrationForm-Container-upper-container-text">
                        <div className="registrationForm-Container-upper-container-first-text">
                            Signing In
                        </div>
                        <div className="registrationForm-Container-upper-container-second-text">
                            Please enter your email and password to login

                        </div>
                    </div>
                </div>
                <Form size='large' loading={this.state.loading} className='formContainer'>
                    <Header as='h2' style={{marginTop: '3%', fontFamily: 'Fahkwang'}} textAlign='center'>
                        Login
                    </Header>
                    <Form.Input
                        fluid icon='mail'
                        iconPosition='left'
                        placeholder='john@concordia.ca'
                        value={this.state.email}
                        error={this.state.errorEmail}
                        onChange={this.changeEmail}
                        label='Email:'/>
                    <Form.Input
                        fluid
                        icon='lock'
                        iconPosition='left'
                        label='Password'
                        placeholder='Password'
                        type='password'
                        value={this.state.password}
                        error={this.state.errorPassword}
                        onChange={this.changePassword}
                    />
                    <Button fluid size='large' style={{marginTop: '10%'}}onClick={this.register}>
                        Login
                    </Button>
                </Form>
            </div>)
        }
    }
}
function mapStateToProps(state){
    return {
        userProfile: state.Reducers.userProfile
    };

}
export default withRouter(connect(mapStateToProps)(RegistrationForm));