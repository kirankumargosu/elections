import { useEffect, useState } from "react";
import  '../css/Districts.css'
 
export default function Districts(props){
    const [tnDistricts, setTnDistricts] = useState([])
    const [selectedDistrict, setSelectedDistrict] = useState(23)
    
    const handleDistrictSelect =  (e) => {
        console.log(e.target.id)
        setSelectedDistrict(parseInt(e.target.id))
        props.onSelectDistrict(parseInt(e.target.id))
    }

    useEffect(() => {
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
        fetchTnDistrictsData();
    }, []);
    return (
        <div>
            {tnDistricts.map((dist, d) => 
                { return (
                    <button className = {dist.district_id==selectedDistrict ? "districtSpanSelected" : "districtSpan"} 
                            key={dist.district_id} 
                            id={dist.district_id}
                            name={dist.district_name}
                            onClick={(e) => {
                                handleDistrictSelect(e) 
                            }}
                            >
                        {dist.district_name}
                    </button>
                    )
                }
        )}
            </div>
    )
}
