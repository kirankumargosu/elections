import  '../css/Parties.css'
import { useEffect, useState } from "react";

export default function Parties(props) {
  const [parties, setParties] = useState([])

  const handlePartySelect =  (e) => {
    setSelectedParty(parseInt(e.target.id))
    props.onSelectParty(parseInt(e.target.id))
  }

    useEffect(() => {
        async function fetchAlliancePartyData() {
            const url = "http://localhost:8000/tamilnadu/alliancePartyData/"+props.selectedAlliance
            try {
                const tnParties = await fetch(url).then(res => res.json());
                // console.log(tnParties)
                setParties(tnParties.data)
            } catch (error) {
                console.log('Error', error)
            }

        }
        fetchAlliancePartyData();
    }, [props]);

  return (
    <>
        {/* <br/> */}
        {parties.map((party, p) => 
          { return (
              <button className = "partySpan"
              style={{backgroundColor : party.colorcode}}
                      key={party.party_id} 
                      >
                {party.party_name}
              </button>
            )
          }
        )}
            {/* {parties.map( (party) => {
                return (
                          <div key={party.party_id}>
                            <button 
                                style={{ backgroundColor:  party.colorcode,
                                         color: '#000000',
                                         font: 'bold',
                                         width : '100px',
                                         marginRight: '5px',
                                         marginBottom: '5px'
                                      }} 
                                key={party.party_id}
                                id={party.party_id}
                                name={party.party_name} 
                                >
                                  {party.party_name}
                                  
                            </button>
                            </div>
                         )
            })} */}
      {/* <br/> */}
    </>
  );
}
