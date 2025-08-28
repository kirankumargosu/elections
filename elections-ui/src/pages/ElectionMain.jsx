import { useEffect, useState } from "react";
import * as React from 'react';
import Tamilnadu from '../components/Tamilnadu'
import Mast from '../components/Mast'
import Legend from '../components/Legend'
import StraightAnglePieChart from '../components/StraightAnglePieChart'
import PieChartWithPaddingAngle from '../components/PieChartWithPaddingAngle'
function ElectionMain() {

    const [selectedParty, setSelectedParty] = useState(1);
    // const [predictedData, setPredictionData] = useState();
    
    const [predictedData, setPredictedData] = React.useState([]);

    useEffect(() => {
        async function fetchPredictedData() {
            console.log("Fetching predicted data")
            const url = "http://localhost:8000/tamilnadu/predictedData"
            try {
                const tnPredictedData = await fetch(url).then(res => res.json());
                setPredictedData(tnPredictedData.data)

            } catch (error) {
                console.log('Error', error)
            }
        }
        fetchPredictedData();
    }, []);

    const handlePredictonData = async () => {
        // console.log("Fetching predicted data from handlePrediction")
        const url = "http://localhost:8000/tamilnadu/predictedData"
            try {
                const tnPredictedData = await fetch(url).then(res => res.json());
                // console.log("tnPredictedData from handlePrectionData", tnPredictedData)
                setPredictedData(tnPredictedData.data)

            } catch (error) {
                console.log('Error', error)
            }
    }
    
    return (
        
        <>
            <Mast />
            <Legend  onSelectParty= {setSelectedParty}/>
            <PieChartWithPaddingAngle predictedData = {predictedData}/>
            <Tamilnadu  selectedParty = {selectedParty} onClickPredict = {handlePredictonData}/>
        </>
    )
}

export default ElectionMain