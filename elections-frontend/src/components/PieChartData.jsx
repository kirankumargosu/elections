import { PieChart } from '@mui/x-charts/PieChart';


function PieChartData(props) {

  // console.log(props);
  return (
    <div>
      <PieChart
        series={[
          {
            startAngle: -90,
            endAngle: 90,
            paddingAngle: 1,
            innerRadius: 20,
            outerRadius: 180,
            cy: '100%',
            data: props['predictedData'],
          },
        ]}
        width={400}
        height={200}
        hideLegend
      />
    </div>
  );
}


export default PieChartData