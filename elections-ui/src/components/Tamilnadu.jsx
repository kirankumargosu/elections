// import { useState } from 'react'
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

const columns = [
  { id: 'district', label: 'District', minWidth: 170 },
  { id: 'constituency_name', label: '\u00a0Constituency', minWidth: 100 },
  {
    id: 'winner_alliance_id_2021',
    label: 'Alliance 2021',
    minWidth: 170,
    align: 'right',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'winner_party_2021',
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

  
  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handlePrediction = (e, constituency_id, constituency_name, winner_alliance_id_2021, winner_party_2021, prediction_2026) => {
    // console.log(props.selectedParty)
    
    let predicted_alliance =  alliances.map((alliance) =>{
      return alliance.alliance_id == props.selectedParty ? alliance.alliance_name : ''})[props.selectedParty-1];
    console.log(predicted_alliance)
    console.log(`${constituency_name} with ID ${constituency_id} has a prediction for 2026 as ${props.selectedParty} which is ${predicted_alliance}`);
    props.onClickPredict({
      constituency_id: constituency_id,
      constituency_name: constituency_name,
      winner_alliance_id_2021: winner_alliance_id_2021,
      winner_party_2021: winner_party_2021,
      prediction_2026: predicted_alliance
    });
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

    // console.log(props.selectedParty)
    return (
    <Paper sx={{ width: '100%', overflow: 'hidden' }}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow>
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
             {main_data
              .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              .map((row, r) => {
                
                return (
                   <TableRow hover role="checkbox" tabIndex={-1} 
                  //  key={row.code}
                  key = {r}
                  code = {row.code}
                   >
                    {columns.map((column, i) => {
                      return (
                        row[column.id] == 'district' ?
                        <TableCell key={i} align={column.align}>
                          {row[column.id]}
                        </TableCell>
                      : column.id == 'winner_alliance_id_2021' ?
                        <TableCell key={i} align={column.align}>
                          {
                          alliances.map((alliance) =>{
                            return (
                            alliance.alliance_id == row[column.id] ? alliance.alliance_name : '' )})
                          }
                        </TableCell>
                        :column.id == 'prediction_2026' ?
                        <TableCell key={i} align={column.align}>
                          <button
                          id = {row.constituency_id}
                          name = {row.constituency_name}
                          style={{ backgroundColor: '#4CAF50', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '4px', cursor: 'pointer' }} 
                          onClick={(e) => {
                            handlePrediction(e, row.constituency_id, row.constituency_name, row.winner_alliance_id_2021, row.winner_party_2021, row.prediction_2026);
                          }}>
                            Click to Predict
                          </button>
                          
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
    )
}

export default Tamilnadu