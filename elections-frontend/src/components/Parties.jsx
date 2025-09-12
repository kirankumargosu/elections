import  '../css/Parties.css'
import { useEffect, useState } from "react";

export default function Parties(props) {
  const [parties, setParties] = useState([])

  // const handlePartySelect =  (e) => {
  //   setSelectedParty(parseInt(e.target.id))
  //   props.onSelectParty(parseInt(e.target.id))
  // }

    useEffect(() => {
        async function fetchAlliancePartyData() {
            const url = process.env.REACT_APP_API_URL + "tamilnadu/alliancePartyData/" + props.selectedAlliance
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
    </>
  );
}
