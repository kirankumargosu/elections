import { useEffect, useState } from "react";
import Tamilnadu from '../components/Tamilnadu'
import Mast from '../components/Mast'
import Legend from '../components/Legend'
import StraightAnglePieChart from '../components/StraightAnglePieChart'
import PieChartWithPaddingAngle from '../components/PieChartWithPaddingAngle'
function ElectionMain() {

    const [selectedParty, setSelectedParty] = useState(1);
    const [predictedData, setPredictionData] = useState();
    
    return (
        
        <>
            <Mast />
            <Legend  onSelectParty= {setSelectedParty}/>

            {/* <StraightAnglePieChart /> */}
            <PieChartWithPaddingAngle predictedData = {predictedData}/>
            <Tamilnadu  selectedParty = {selectedParty} onClickPredict = {setPredictionData}/>
        </>
    )
}

export default ElectionMain