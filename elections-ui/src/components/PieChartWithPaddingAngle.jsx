import * as React from 'react';
import Stack from '@mui/material/Stack';
import { PieChart } from '@mui/x-charts/PieChart';


const data = [
  { label: 'DMK+', value: 120, color: '#FF0000' },
  { label: 'NDA', value: 70, color: '#e39c39ff' },
  { label: 'TVK+', value: 20, color: '#FFFF00'},
  { label: 'NTK', value: 10, color: '#db624d' },
  { label: 'Others', value: 2, color: '#D3D3D3' },
];


export default function PieChartWithPaddingAngle(props) {
  

  console.log(props['data']);
  return (
    <div>
    {/* <Stack width="100%" direction="row" flexWrap="wrap"> */}
      {/* <PieChart
        series={[
          {
            paddingAngle: 5,
            innerRadius: 60,
            outerRadius: 80,
            data,
          },
        ]}
        width={200}
        height={200}
        hideLegend
      /> */}
      <PieChart
        series={[
          {
            startAngle: -90,
            endAngle: 90,
            paddingAngle: 3,
            innerRadius: 100,
            outerRadius: 600,
            cy: '100%',
            data,
          },
        ]}
        width={3000}
        height={400}
        hideLegend
      />
    {/* </Stack> */}
    {/* <br /> */}
    </div>
  );
}
