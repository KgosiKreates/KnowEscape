import ServiceCategoryPage from '@/components/ServiceCategoryPage'
import { servicePages } from '@/util/servicePages'

export const metadata = {
    title: 'Skills Development | Knowescape Consulting',
    description: servicePages['skills-development'].introduction,
}

export default function SkillsDevelopmentPage() {
    return <ServiceCategoryPage service={servicePages['skills-development']} />
}
