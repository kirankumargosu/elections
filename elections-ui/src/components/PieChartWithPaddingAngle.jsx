import { useEffect, useState } from "react";
import * as React from 'react';
import Stack from '@mui/material/Stack';
import { PieChart } from '@mui/x-charts/PieChart';


// const data = [
//   { label: 'DMK+', value: 120, color: '#FF0000' },
//   { label: 'NDA', value: 70, color: '#e39c39ff' },
//   { label: 'TVK+', value: 20, color: '#FFFF00'},
//   { label: 'NTK', value: 10, color: '#db624d' },
//   { label: 'Others', value: 2, color: '#D3D3D3' },
// ];


function PieChartWithPaddingAngle(props) {

  console.log(props['data']);
  return (
    <div>
      <PieChart
        series={[
          {
            startAngle: -90,
            endAngle: 90,
            paddingAngle: 3,
            innerRadius: 100,
            outerRadius: 600,
            cy: '90%',
            data: props['predictedData'],
          },
        ]}
        width={3000}
        height={400}
        hideLegend
      />
    </div>
  );
}


export default PieChartWithPaddingAngle