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

const columns = [
  { id: 'district', label: 'District', minWidth: 170 },
  { id: 'constituency_name', label: '\u00a0Constituency', minWidth: 100 },
  {
    id: 'winner_party_2021',
    label: 'Alliance 2021',
    minWidth: 170,
    align: 'right',
    format: (value) => value.toLocaleString('en-US'),
  },
  {
    id: 'winner_alliance_id_2021',
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
function Tamilnadu () {
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };


    return (<Paper sx={{ width: '100%', overflow: 'hidden' }}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow>
              {columns.map((column) => (
                <TableCell
                  key={column.constituency_id}
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
              .map((row) => {
                return (
                   <TableRow hover role="checkbox" tabIndex={-1} key={row.code}>
                    {columns.map((column) => {
                      
                      return (
                        row[column.id] == 'district' ?
                        <TableCell key={column.id} align={column.align}>
                          {column.format && typeof row[column.id] === 'number'
                            ? column.format(row[column.id])
                            : row[column.id]}
                        </TableCell>
                      :
                        <TableCell key={column.id} align={column.align}>
                          {column.format && typeof row[column.id] === 'number'
                            ? column.format(row[column.id])
                            : row[column.id]}
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