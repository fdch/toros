import { Typography } from '@mui/material';
import React, { useEffect, useState } from 'react';
import DealType from '../types/DealType';

interface DealProps {
    company_id: bigint;
}

const Deals: React.FC<DealProps> = ({ company_id }) => {

    const [data, setData] = useState<DealType[]>([])

    useEffect(() => {
        fetch(`http://localhost:20002/deals_by_company/${company_id}`, {
            headers: {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }
        })
            .then((response) => {
                console.log(response);
                return response.json();
            }).then(resjson => {
                setData(resjson);
            });
    }, []);

    return (
        <div>
            {data && data.length > 0 && <div>
                <Typography sx={{ mb: 0.8 }} color="text.primary">Deals</Typography>
                {data.map((deal, index) => (
                    <div key={index}>
                        <Typography sx={{ mb: 0.5 }} color="text.secondary">
                            {deal.date + ": $" + deal.funding_amount + " - " + deal.funding_round}
                        </Typography>
                    </div>

                ))}
            </div>}

        </div>
    );
};

export default Deals;
