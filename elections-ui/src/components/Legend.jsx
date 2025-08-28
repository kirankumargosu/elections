import  '../css/Legend.css'
import { useState } from "react";
import Grid from '@mui/material/Grid';
import alliances from '../static/tamilnadu/alliances';


export default function Legend(props) {
  const [selectedParty, setSelectedParty] = useState(1)
  const handlePartySelect =  (e) => {
    setSelectedParty(e.target.id)
    props.onSelectParty(e.target.id)
  }

  return (
    <>
    {/* {console.log(selectedParty)}
    {console.log(props)} */}
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
