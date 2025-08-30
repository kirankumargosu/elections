import { useEffect, useState } from "react";
import * as React from 'react';
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

function ElectionMain() {

    const [selectedAlliance, setSelectedAlliance] = useState(1);
    const [predictedData, setPredictedData] = React.useState([]);

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
    
    return (
        
        <>
            <Mast />
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                <TableHead>
                    <TableRow sx={{
                  "& th": {
                  color: '#f1f1f7ff',
                  backgroundColor: '#0c4a13ff',
                  font: 'bold',
                  fontfamily: 'Arial',
                  fontSize: 16
                }
              }}>  
                        <TableCell align="center" width={"20%"}>Alliances</TableCell>
                        <TableCell align="center" width={"60%"}>Prediction</TableCell>
                        <TableCell align="center" width={"20%"}>Parties</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    <TableRow>  
                        <TableCell align="center">
                            <Alliances onSelectAlliance= {handleAllianceChange}/>
                        </TableCell>
                        <TableCell align="center">
                            <PieChartData predictedData = {predictedData}/>
                        </TableCell>
                        <TableCell align="center">
                            <Parties selectedAlliance = {selectedAlliance}/>
                        </TableCell>
                    </TableRow>
                </TableBody>
            </Table>
            <Tamilnadu selectedAlliance = {selectedAlliance} onClickPredict = {handlePredictonData}/>
        </>
    )
}

export default ElectionMain