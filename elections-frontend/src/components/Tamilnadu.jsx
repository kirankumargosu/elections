import { useEffect, useState } from "react";
import '../css/Tamilnadu.css'

import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Button from "@mui/material/Button";

function Tamilnadu (props) {
  const [tnData, setTnData] = useState([])
  const [tnAllianceColorCode, setTnAllianceColorCode] = useState({})

  useEffect(() => {
    async function fetchTnStaticData() {
      const url = process.env.REACT_APP_API_URL + "tamilnadu/static/" 
      try {
        const tns = await fetch(url).then(res => res.json());
        setTnData(tns.data)

      } catch (error) {
        console.log('Error', error)
      }
    }

    async function fetchTnAlliancesColorCodeData() {
      const url = process.env.REACT_APP_API_URL + "tamilnadu/allianceColorCode/" 
      try {
        const tns = await fetch(url).then(res => res.json());
        setTnAllianceColorCode(tns.data)
        // console.log("tnAllianceColorCode", tns.data)
      } catch (error) {
        console.log('Error', error)
      }
    }

    fetchTnStaticData();
    fetchTnAlliancesColorCodeData();
  }, []);

  const handlePrediction = async (e, constituency_id, mode) => {
    try{
        const url = process.env.REACT_APP_API_URL + "tamilnadu/updatePrediction" 
        const tns = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=utf-8",
            },
            body: JSON.stringify({
                constituency_id: constituency_id,
                prediction_alliance_id_next: (mode === "update") ? props.selectedAlliance : -1}),
          }).then(res => res.json());
          setTnData(tns.data)
          props.onClickPredict()
        } catch (error) {
        console.log('Error', error)
    }
  };

  const handleClearAll = async () => {
    try{
      const url = process.env.REACT_APP_API_URL + "tamilnadu/resetPrediction/" 
      const tns = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
        },
        body: JSON.stringify(),
      }).then(res => res.json());
      setTnData(tns.data)
          
      props.onClickPredict()
    } 
    catch (error) {
        console.log('Error', error)
    }
  }
  const handlePrevElectionClick = async () => {
    const url = process.env.REACT_APP_API_URL + "tamilnadu/prevResults"
    try {
      const tns = await fetch(url).then(res => res.json());
      setTnData(tns.data)
      props.onClickPredict()

    } catch (error) {
      console.log('Error', error)
    }
  }
    
    return (
      <>
        <br/>
        <Button variant="text" onClick={handleClearAll}>Clear All </Button>
        <Button variant="text" onClick={handlePrevElectionClick}>Prev. Result</Button>

        <TableContainer sx={{maxHeight: 1000}}>
          <Table stickyHeader aria-label="sticky table">
            <TableHead>
              <TableRow 
                sx={{
                      "& th": {
                      color: '#f1f1f7ff',
                      backgroundColor: '#0f0fd4ff',
                      font: 'bold',
                      fontfamily: 'Arial',
                      fontSize: 20
                    }
                  }}>
                
                <TableCell>
                  District
                </TableCell>
                
                <TableCell>
                  Constituency
                </TableCell>

                <TableCell>
                  Alliance 2021
                </TableCell>
                
                <TableCell>
                  Winner 2021
                </TableCell>
                
                <TableCell>
                  Prediction
                </TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
              {tnData.map((row, r) => {
                return (
                  row['district_id'] === props.selectedDistrict &&
                  <TableRow 
                    style = {{'maxheight': '10px', 'background': tnAllianceColorCode[row.prediction_alliance_id_next]}}
                    key = {r}
                    code = {row.code}
                  >
                    <TableCell
                    style = {{width: '15%'}}>
                      {row.district}
                    </TableCell>

                    <TableCell 
                    style = {{width: '30%'}}>
                      {row.constituency_name}
                    </TableCell>

                    <TableCell
                    style = {{width: '20%'}}>
                      {row.winner_alliance_prev}
                    </TableCell>

                    <TableCell
                    style = {{width: '20%'}}>
                      {row.winner_party_prev}
                    </TableCell>

                    <TableCell>
                      {row.prediction_alliance_id_next === -1 ?
                        <button className="predictButton"
                          id = {row.constituency_id}
                          name = {row.constituency_name}
                          onClick={(e) => {
                            handlePrediction(e, row.constituency_id, 'update');
                          }}
                        >
                          Click to Predict
                        </button>
                        :
                        <button className="predictButton"
                          id = {row.constituency_id}
                          name = {row.constituency_name}
                          style={{ backgroundColor: tnAllianceColorCode[row.prediction_alliance_id_next], color: 'black', border: '2px solid black', borderRadius: '4px'}} 
                          onClick={(e) => {
                            handlePrediction(e, row.constituency_id, 'reset');
                          }}
                        >
                          Reset Prediction
                        </button>
                      }
                    </TableCell>
                  </TableRow>
                );
              })}
              <TableRow>
              </TableRow>
            </TableBody>
          </Table>
        </TableContainer>
      </>
    )
}

export default Tamilnadu