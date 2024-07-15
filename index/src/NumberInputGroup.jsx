import NumberInput from "./NumberInput";
import { useState, queryString } from "react";

const NumberInputGroup = ({ setSubmitted }) => {
    //state to store all input boxes    
    const [inputValues, setInputValues] = useState({
        input1: '',
        input2: '',
        input3: '',
        input4: '',
        input5: '',
        input6: '',
        input7: '',
        input8: '',
        input9: '',
        input10: '',
        // Add more input values here
    });
    //this function updates the value of the state inputValues
    const handleInputChange = (inputId, value) => {
        setInputValues((prevInputValues) => ({
            ...prevInputValues,
            [inputId]: value,
        }));
    };
    //this function processes form submission
    const handleSubmit = async () => {
        event.preventDefault()
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone_no: "7970460076" })
        };
        const response = await fetch(import.meta.env.VITE_BACKEND_BASE_URL + '/marketing/callbackrequest/', requestOptions);
        const data = await response.json();
        setSubmitted(true)
        // this.setState({ postId: data.id });
    };
    //return child component
    return (
        <>
            <div id='NumberInputGroup' className="flex justify-center lg:space-x-2" data-autosubmit="true">
                <div className="flex flex-col lg:flex-row justify-center space-y-2 lg:space-y-0 lg:space-x-2">
                    <div className="flex flex-row space-x-2">
                        <NumberInput
                            id="input1"
                            value={inputValues.input1}
                            onValueChange={handleInputChange}
                            previousId={null}
                            handleSubmit={handleSubmit}
                            nextId="input2"
                        />
                        <NumberInput
                            id="input2"
                            value={inputValues.input2}
                            onValueChange={handleInputChange}
                            previousId="input1"
                            handleSubmit={handleSubmit}
                            nextId="input3"
                        />
                        <NumberInput
                            id="input3"
                            value={inputValues.input3}
                            onValueChange={handleInputChange}
                            previousId="input2"
                            handleSubmit={handleSubmit}
                            nextId="input4"
                        />
                        {/* Seperator */}
                        <span className=" flex flex-col justify-center">&nbsp;</span>
                        <NumberInput
                            id="input4"
                            value={inputValues.input4}
                            onValueChange={handleInputChange}
                            previousId="input3"
                            handleSubmit={handleSubmit}
                            nextId="input5"
                        />
                        <NumberInput
                            id="input5"
                            value={inputValues.input5}
                            onValueChange={handleInputChange}
                            previousId="input4"
                            handleSubmit={handleSubmit}
                            nextId="input6"
                        />
                    </div>
                    <div className="flex flex-row space-x-2">
                        <NumberInput
                            id="input6"
                            value={inputValues.input6}
                            onValueChange={handleInputChange}
                            previousId="input5"
                            handleSubmit={handleSubmit}
                            nextId="input7"
                        />
                        <NumberInput
                            id="input7"
                            value={inputValues.input7}
                            onValueChange={handleInputChange}
                            previousId="input6"
                            handleSubmit={handleSubmit}
                            nextId="input8"
                        />
                        <span className="flex flex-col justify-center">&nbsp;</span>
                        <NumberInput
                            id="input8"
                            value={inputValues.input8}
                            onValueChange={handleInputChange}
                            previousId="input7"
                            handleSubmit={handleSubmit}
                            nextId="input9"
                        />
                        <NumberInput
                            id="input9"
                            value={inputValues.input9}
                            onValueChange={handleInputChange}
                            previousId="input8"
                            handleSubmit={handleSubmit}
                            nextId="input10"
                        />
                        <NumberInput
                            id="input10"
                            value={inputValues.input10}
                            onValueChange={handleInputChange}
                            previousId="input9"
                            handleSubmit={handleSubmit}
                        />
                    </div>
                </div>
            </div>
        </>
    );
}

export default NumberInputGroup;