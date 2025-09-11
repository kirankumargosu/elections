import { useEffect, useState } from "react";
import '../css/Tamilnadu.css'

import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import Button from "@mui/material/Button";
import Tab from "@mui/material/Tab";

const columns = [
  // { id: 'SNo', label: 'S.No', minWidth: 10 },
  { id: 'district', label: 'District', minWidth: 170 },
  { id: 'constituency_name', label: '\u00a0Constituency', minWidth: 100 },
  {
    id: 'winner_alliance_prev',
    label: 'Alliance 2021',
    minWidth: 170,
    align: 'right',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'winner_party_prev',
    label: 'Winner 2021',
    minWidth: 170,
    align: 'right',
    format: (value) => value.toLocaleString('en-US'),
  },

  {
    id: 'prediction_2026',
    label: 'Prediction',
    minWidth: 170,
    align: 'right',
    format: (value) => value.toFixed(2),
  },
];
function Tamilnadu (props) {
  const [tnData, setTnData] = useState([])
  const [tnAllianceColorCode, setTnAllianceColorCode] = useState({})

  useEffect(() => {
    async function fetchTnStaticData() {
      const url = "http://localhost:8000/tamilnadu/static"
      try {
        const tns = await fetch(url).then(res => res.json());
        setTnData(tns.data)

      } catch (error) {
        console.log('Error', error)
      }
    }

    async function fetchTnStaticDataForDistrict() {
      const url = "http://localhost:8000/tamilnadu/static/" + props.selectedDistrict
      try {
        const tns = await fetch(url).then(res => res.json());
        console.log(tns.data)
        setTnDataForDistrict(tns.data)

      } catch (error) {
        console.log('Error', error)
      }
    }

    async function fetchTnAlliancesColorCodeData() {
      const url = "http://localhost:8000/tamilnadu/allianceColorCode" 
      try {
        const tns = await fetch(url).then(res => res.json());
        setTnAllianceColorCode(tns.data)
        // console.log("tnAllianceColorCode", tns.data)
      } catch (error) {
        console.log('Error', error)
      }
    }

    async function fetchTnDistrictsData() {
      const url = "http://localhost:8000/tamilnadu/districts" 
      try {
        const tns = await fetch(url).then(res => res.json());
        // list.sort((a, b) => (a.qty > b.qty) ? 1 : -1)
        // console.log(tns.data)
        tns.data.sort((a, b) => (a.district_name > b.district_name) ? 1 : -1)
        // console.log(a)
        setTnDistricts(tns.data)
      } catch (error) {
        console.log('Error', error)
      }
    }

    fetchTnStaticData();
    fetchTnDistrictsData();
    // fetchTnStaticDataForDistrict();
    fetchTnAlliancesColorCodeData();
  }, []);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handlePrediction = async (e, constituency_id, mode) => {
    try{
        const tns = await fetch("http://localhost:8000/tamilnadu/updatePrediction", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=utf-8",
            },
            body: JSON.stringify({
                constituency_id: constituency_id,
                prediction_alliance_id_next: (mode == "update") ? props.selectedAlliance : -1}),
          }).then(res => res.json());
          setTnData(tns.data)
          props.onClickPredict()
        } catch (error) {
        console.log('Error', error)
    }
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  const handleClearAll = async () => {
    try{
      const tns = await fetch("http://localhost:8000/tamilnadu/resetPrediction", {
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
          const url = "http://localhost:8000/tamilnadu/prevResults"
      try {
        const tns = await fetch(url).then(res => res.json());
        setTnData(tns.data)
        props.onClickPredict()

      } catch (error) {
        console.log('Error', error)
      }
  }

  
  const fetchTnStaticDataForDistrict = async () => {
      console.log(props.selectedDistrict)
      const url = "http://localhost:8000/tamilnadu/static/" + props.selectedDistrict
      try {
        const tns = await fetch(url).then(res => res.json());
        console.log(tns.data)
        setTnDataForDistrict(tns.data)

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
                  row['district_id'] == props.selectedDistrict &&
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
                      {row.prediction_alliance_id_next == -1 ?
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