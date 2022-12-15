import Deals from './Deals';
import CompanyType from '../types/CompanyType';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

interface CompanyProps {
    company: CompanyType
}
const Company: React.FC<CompanyProps> = ({ company }): JSX.Element => {

    return (
        <Card sx={{ minWidth: 275 }}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Company
                </Typography>
                <Typography variant="h5" component="div">
                    {company.name}
                </Typography>
                <Typography sx={{ mb: 1.5 }} color="text.secondary">
                    {company.country}
                </Typography>
                <Typography variant="body2">
                    {company.description}
                </Typography>
                <Typography variant="body2">
                    {/* {founding_date} */}
                </Typography>
                <Deals company_id={company.company_id} />
            </CardContent>
            <CardActions>

            </CardActions>
        </Card>
    );
}

export default Company;