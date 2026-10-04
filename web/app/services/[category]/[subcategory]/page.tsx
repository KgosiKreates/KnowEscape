import { notFound, redirect } from 'next/navigation'

const bbbeeSections: Record<string, string> = {
    assessment: 'bbbee-assessment-readiness',
    compliance: 'bbbee-compliance-support',
    scorecard: 'bbbee-scorecard-support',
    transformation: 'bbbee-transformation-advisory',
}

type PageProps = {
    params: Promise<{ category: string; subcategory: string }>
}

export function generateStaticParams({ params }: { params: { category: string } }) {
    if (params.category !== 'bbbee-advisory') return []

    return Object.keys(bbbeeSections).map((subcategory) => ({ subcategory }))
}

export default async function ServiceSubcategoryRedirect({ params }: PageProps) {
    const { category, subcategory } = await params
    const section = category === 'bbbee-advisory' ? bbbeeSections[subcategory] : undefined

    if (!section) notFound()

    redirect(`/services/bbbee-advisory#${section}`)
}
