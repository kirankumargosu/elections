import  '../css/Alliances.css'
import { useEffect, useState } from "react";
import * as React from 'react';

export default function Alliances(props) {
  const [selectedAlliance, setSelectedAlliance] = useState(1)
  const handleAllianceSelect =  (e) => {
    setSelectedAlliance(parseInt(e.target.id))
    props.onSelectAlliance(parseInt(e.target.id))
  }
    const [allianceData, setAllianceData] = React.useState([])

    useEffect(() => {
        async function fetchAllianceData() {
            const url = "http://localhost:8000/tamilnadu/alliances"
            try {
                const tnAllianceData = await fetch(url).then(res => res.json());
                // console.log("tnAllianceData ", tnAllianceData)
                setAllianceData(tnAllianceData.data)

            } catch (error) {
                console.log('Error', error)
            }

        }
        fetchAllianceData();
    }, []);

  return (
    <>
        <br/>
            {allianceData.map( (alliance) => {
                return (
                          selectedAlliance == alliance.alliance_id ?
                          <div key={alliance.alliance_id}>
                            <button 
                                style={{ backgroundColor:  alliance.colorcode,
                                         color: '#000000',
                                         font: 'bold',
                                         width : '100px',
                                         marginRight: '5px',
                                         marginBottom: '5px'
                                      }} 
                                key={alliance.alliance_id}
                                id={alliance.alliance_id}
                                name={alliance.alliance_name}
                                onClick={(e) => handleAllianceSelect(e)} 
                                >
                                  {alliance.alliance_name}
                                  
                            </button>
                            </div>
                         :
                         <div key={alliance.alliance_id}>
                            <button 
                                style={{ backgroundColor:  '#000000',
                                         color: '#ffffff',
                                         font: 'bold',
                                         width : '100px',
                                         marginRight: '5px',
                                         marginBottom: '5px'
                                      }} 
                                key={alliance.alliance_id}
                                id={alliance.alliance_id}
                                name={alliance.alliance_name}
                                onClick={(e) => handleAllianceSelect(e)} 
                                >
                                  {alliance.alliance_name}
                                  
                            </button>
                            </div>
                         )
            })}
      <br/>
    </>
  );
}
