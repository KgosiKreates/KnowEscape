import ServiceCategoryPage from '@/components/ServiceCategoryPage'
import { servicePages } from '@/util/servicePages'

export const metadata = {
    title: 'Enterprise & Supplier Development | Knowescape Consulting',
    description: servicePages['enterprise-supplier-development'].introduction,
}

export default function EnterpriseSupplierDevelopmentPage() {
    return <ServiceCategoryPage service={servicePages['enterprise-supplier-development']} />
}
