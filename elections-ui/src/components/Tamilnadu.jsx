import { useEffect, useState } from "react";
import * as React from 'react';
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

const columns = [
  { id: 'SNo', label: 'S.No', minWidth: 10 },
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
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(50);
  const [tnData, setTnData] = React.useState([])
  const [tnAllianceColorCode, setTnAllianceColorCode] = React.useState({})
  const [tnDistricts, setTnDistricts] = React.useState([])
  const [selectedDistrict, setSelectedDistrict] = React.useState(23)

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

    // async function fetchTnAlliancesData() {
    //   const url = "http://localhost:8000/tamilnadu/alliances" 
    //   try {
    //     const tns = await fetch(url).then(res => res.json());
    //     setTnAlliances(tns.data)

    //   } catch (error) {
    //     console.log('Error', error)
    //   }
    // }

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
    // fetchTnAlliancesData();
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

  const handleDistrictSelect = async (dist) => {
    // console.log(dist)
    setSelectedDistrict(dist)
  }
    
    // console.log(props.selectedParty)
    return (
      <>
        {tnDistricts.map((dist, d) => 
          { return (
              <button className = {dist.district_id==selectedDistrict ? "districtSpanSelected" : "districtSpan"} 
                      key={dist.district_id} 
                      onClick={(e) => {
                        handleDistrictSelect(dist.district_id)
                      }}
                      >
                {dist.district_name}
              </button>
            )
          }
        )}
        <br/>
        <Button variant="text" onClick={handleClearAll}>Clear All </Button>

        <TableContainer sx={{maxHeight: 400}}>
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
                  S.No
                </TableCell>
                
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
          </Table>
        </TableContainer>
        

        <Paper sx={{ width: '100%', overflow: 'hidden' }}>
          <TableContainer sx={{ maxHeight: 440 }}>
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
                  }}
                >
                  {columns.map((column, c) => (
                    <TableCell
                      key={c}
                      align={column.align}
                      style={{ minWidth: column.minWidth, font: 'bold' }}
                    >
                      {column.label}
                    </TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {tnData
                  .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                  .map((row, r) => {
                    
                    // tnData['district_id'] == selectedDistrict &&
                    return (
                      <TableRow hover role="checkbox" tabIndex={-1} 
                        style = {{'background': tnAllianceColorCode[row.prediction_alliance_id_next]}}
                        key = {r}
                        code = {row.code}
                      >
                        {columns.map((column, i) => {
                          return (
                            row[column.id] == 'district' ?
                              <TableCell key={i} align={column.align}>
                                {row[column.id]}
                              </TableCell>
                            : column.id == 'winner_alliance_id_prev' ?
                              <TableCell key={i} align={column.align}>
                                {row[column.id]}
                              </TableCell>
                            :column.id == 'prediction_2026' ?
                              <TableCell key={i} align={column.align}>
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
                                  <button
                                  id = {row.constituency_id}
                                  name = {row.constituency_name}
                                  style={{ backgroundColor: tnAllianceColorCode[row.prediction_alliance_id_next], color: 'black', padding: '10px 20px', border: '2px solid black', borderRadius: '4px', cursor: 'pointer' }} 
                                  onClick={(e) => {
                                    handlePrediction(e, row.constituency_id, 'reset');
                                  }}
                                >
                                  Reset Prediction
                                </button>
                                }
                              
                            </TableCell>
                            :<TableCell key={i} align={column.align}>
                              {row[column.id]}
                            </TableCell>
                          );
                        })}
                      </TableRow>
                    );
                  })}
              </TableBody>
            </Table>
          </TableContainer>
          <TablePagination
            rowsPerPageOptions={[50, 100]}
            component="div"
            count={tnData.length}
            rowsPerPage={rowsPerPage}
            page={page}
            onPageChange={handleChangePage}
            onRowsPerPageChange={handleChangeRowsPerPage}
          />
        </Paper>
      </>
    )
}

export default Tamilnadu