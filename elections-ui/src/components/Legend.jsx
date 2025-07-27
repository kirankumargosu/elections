import  '../css/Legend.css'
import { useEffect, useState } from "react";
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
// import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import alliances from '../static/tamilnadu/alliances';
// const alliances = [
//     {'id': 1, 'name': 'DMK+', 'colorcode': '#FF0000'},
//     {'id': 2, 'name': 'AIDMK+', 'colorcode': '#00FF00'},
//     {'id': 3, 'name': 'TVK', 'colorcode': '#FFFF00'},
//     {'id': 4, 'name': 'Others', 'colorcode': '#D3D3D3'}
// ]



export default function Legend() {
  const [selectedParty, setSelectedParty] = useState(1)

  const handlePartySelect =  (e) => {
    console.log(e.target.id)
    console.log(e.target.name)
    setSelectedParty(e.target.id)
  }

  return (
    <>
        <br/>
        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
            {alliances.map( (party) => {
                return (
                          selectedParty == party.alliance_id ?
                            <button 
                                style={{ backgroundColor:  party.colorcode,
                                         color: '#000000',
                                         font: 'bold'
                                      }} 
                                key={party.alliance_id}
                                id={party.alliance_id}
                                name={party.alliance_name}
                                onClick={(e) => handlePartySelect(e)} 
                                >
                                  {party.alliance_name}
                                  
                            </button>
                         
                         :
                         
                            <button 
                                style={{ backgroundColor:  '#000000',
                                         color: '#ffffff',
                                         font: 'bold'
                                      }} 
                                key={party.alliance_id}
                                id={party.alliance_id}
                                name={party.alliance_name}
                                onClick={(e) => handlePartySelect(e)} 
                                >
                                  {party.alliance_name}
                                  
                            </button>
                         )
            })}
        </Grid>
      <br/>
    </>
  );
}
