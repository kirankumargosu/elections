import { useEffect, useState } from "react";
import * as React from 'react';

import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import main_data from '../static/tamilnadu/data';
import parties from '../static/tamilnadu/parties';
import alliances from '../static/tamilnadu/alliances';
import Button from "@mui/material/Button";
const columns = [
  { id: 'district', label: 'District', minWidth: 170 },
  { id: 'constituency_name', label: '\u00a0Constituency', minWidth: 100 },
  {
    id: 'winner_alliance_id_prev',
    label: 'Alliance 2021',
    minWidth: 170,
    align: 'right',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'winner_party_prev',
    label: 'Party 2021',
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
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const [tnStatic, setTnStatic] = React.useState([])
  const [tnAlliances, setTnAlliances] = React.useState(alliances)
  const [tnAllianceColorCode, setTnAllianceColorCode] = React.useState({})

  useEffect(() => {
    async function fetchTnStaticData() {
      const url = "http://localhost:8000/tamilnadu/static"
      try {
        const tns = await fetch(url).then(res => res.json());
        setTnStatic(tns.data)

      } catch (error) {
        console.log('Error', error)
      }
    }

    async function fetchTnAlliancesData() {
      const url = "http://localhost:8000/tamilnadu/alliances" 
      try {
        const tns = await fetch(url).then(res => res.json());
        setTnAlliances(tns.data)

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
    fetchTnStaticData();
    fetchTnAlliancesData();
    fetchTnAlliancesColorCodeData();
  }, []);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handlePrediction = async (e, constituency_id, mode) => {
    // console.log("selectedParty", props.selectedParty)
    try{
        const tns = await fetch("http://localhost:8000/tamilnadu/updatePrediction", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=utf-8",
            },
            body: JSON.stringify({
                constituency_id: constituency_id,
                prediction_alliance_id_next: (mode == "update") ? props.selectedParty : -1}),
          }).then(res => res.json());
          setTnStatic(tns.data)
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
      setTnStatic(tns.data)
          
      props.onClickPredict()
    } 
    catch (error) {
        console.log('Error', error)
    }
  }
    
    // console.log(props.selectedParty)
    return (
      <>
      
                  <Button variant="text" onClick={handleClearAll}>Clear All </Button>
      
    <Paper sx={{ width: '100%', overflow: 'hidden' }}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow
            // style = {{'background': '#0f0fd4ff', 'color': '#FFFFFF'}}
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
                  // key={column.constituency_id}
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
             {tnStatic
              .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              .map((row, r) => {
                
                return (
                   <TableRow hover role="checkbox" tabIndex={-1} 
                  //  backgroundColor = '#FF0000'
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
                            {
                              alliances.map((alliance) =>{
                                return (
                                  alliance.alliance_id == row[column.id] ? alliance.alliance_name : '' )})
                            }
                          </TableCell>
                        :column.id == 'prediction_2026' ?
                          <TableCell key={i} align={column.align}>
                            {row.prediction_alliance_id_next == -1 ?
                            <button
                              id = {row.constituency_id}
                              name = {row.constituency_name}
                              style={{ backgroundColor: '#4CAF50', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '4px', cursor: 'pointer' }} 
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
                              {/* {tnAllianceColorCode[row.prediction_alliance_id_next]} */}
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
        rowsPerPageOptions={[10, 25, 100]}
        component="div"
        count={main_data.length}
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