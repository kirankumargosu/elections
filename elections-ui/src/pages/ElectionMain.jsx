import { useEffect, useState } from "react";
import '../css/ElectionMain.css'

import Tamilnadu from '../components/Tamilnadu'
import Mast from '../components/Mast'
import Alliances from '../components/Alliances';
import Parties from "../components/Parties";
import PieChartData from '../components/PieChartData'
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableRow from "@mui/material/TableRow";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import Districts from "../components/Districts";

function ElectionMain() {

    const [selectedAlliance, setSelectedAlliance] = useState(1);
    const [predictedData, setPredictedData] = useState([]);
    const [selectedDistrict, setSelectedDistrict] = useState(23);

    useEffect(() => {
        async function fetchPredictedData() {
            const url = "http://localhost:8000/tamilnadu/predictedData"
            try {
                const tnPredictedData = await fetch(url).then(res => res.json());
                setPredictedData(tnPredictedData.data)

            } catch (error) {
                console.log('Error', error)
            }
        }
        fetchPredictedData();
    }, [selectedAlliance]);

    const handlePredictonData = async () => {
        // console.log("Fetching predicted data from handlePrediction")
        const url = "http://localhost:8000/tamilnadu/predictedData"
            try {
                const tnPredictedData = await fetch(url).then(res => res.json());
                setPredictedData(tnPredictedData.data)

            } catch (error) {
                console.log('Error', error)
            }
    }

    const handleAllianceChange = async (allianceId) => {
        // console.log("alliance changed", allianceId)
        setSelectedAlliance(allianceId)
    }
    
    const handleDistrictChange = async (districtId) => {
        // console.log("district changed", districtId)
        setSelectedDistrict(districtId)
    }

    return (
        
        <>
            <Mast />
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                <TableHead>
                    <TableRow style = {{backgroundColor:"#1b1b1b"}}>  
                        <TableCell style = {{color:"#f3f3daff", fontSize:"20px", fontWeight:"bold"}} align="center" width={"20%"}>Alliances</TableCell>
                        <TableCell style = {{color:"#f3f3daff", fontSize:"20px", fontWeight:"bold"}} align="center" width={"60%"}>Prediction</TableCell>
                        <TableCell style = {{color:"#f3f3daff", fontSize:"20px", fontWeight:"bold"}}  align="center" width={"20%"}>Parties</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    <TableRow>  
                        <TableCell align="center" style={{ minWidth: 100}}>
                            <Alliances onSelectAlliance= {handleAllianceChange}/>
                        </TableCell>
                        <TableCell align="center">
                            <PieChartData predictedData = {predictedData}/>
                        </TableCell>
                        <TableCell align="center" style={{ minWidth: 400}}>
                            <Parties selectedAlliance = {selectedAlliance}/>
                        </TableCell>
                    </TableRow>
                </TableBody>
            </Table>
            <Districts onSelectDistrict = {handleDistrictChange}/>
            <Tamilnadu selectedAlliance = {selectedAlliance} selectedDistrict = {selectedDistrict} onClickPredict = {handlePredictonData}/>
        </>
    )
}

export default ElectionMain