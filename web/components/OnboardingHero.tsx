import images from '../util/imports'
import Image from "next/image"
import Link from 'next/link'
import { Marquee } from "./ui/marquee"
import type { ImageProps } from "next/image"
import '../styles/onboardingHero.css'

import { Badge } from './ui/badge'
import { TextAnimate } from './ui/text-animate'
import { BlurFade } from "@/components/ui/blur-fade"
import { WordRotate } from "@/components/ui/word-rotate"

import {ArrowUpRight, BadgeCheck} from "lucide-react"


const firstRow = images.slice(0, 5)
const secondRow = images.slice(5)

const MarqueeImage = ({img}: {img:ImageProps["src"]}) => {

    return (
        <div className="marquee-image">
            <Image 
                alt=""
                src={img}
                fill
                loading="lazy"
            />
        </div>
    )
}

export default function OnboardingHero () {

    return (
        <section id="onboardingHero">
            <div className="text-content">
                <Badge variant="outline" className='site-badge'>
                    <BadgeCheck data-icon="inline-start" />
                    Our Guarantee
                </Badge>
                <h2 className="site-heading">
                    Your business can do more than just survive.
                    <span> It can <WordRotate words={["Thrive", "Succeed", "Develop", "Grow"]} /></span>
                </h2>
                <TextAnimate by='word' as='p' className='site-body' animation='blurInUp'>
                    From Skills Development and Enterprise & Supplier 
                    Development to business support and growth opportunities, 
                    Knowescape Consulting helps organisations develop their 
                    people, strengthen compliance, improve business capability, 
                    and build a foundation for sustainable growth.
                </TextAnimate>
                <BlurFade className="actions" inView inViewMargin='0px' direction='right'>
                    {/* Application intake is not ready yet.
                    <Link href='/' className="site-btn primary">
                        Apply
                    </Link>
                    */}
                    <Link className="site-link primary" href={'/'}>
                        Our Services
                        <ArrowUpRight />
                    </Link>
                </BlurFade>
            </div>
            <div className="img-marquee">
                <Marquee className="[--duration:20s]">
                    {firstRow.map((img_url, index) => (
                    <MarqueeImage key={index} img={img_url}/>
                    ))}
                </Marquee>
                <Marquee reverse className="[--duration:20s]">
                    {secondRow.map((img_url, index) => (
                    <MarqueeImage key={index} img={img_url}/>
                    ))}
                </Marquee>
                <div className="from-background pointer-events-none absolute inset-y-0 left-0 w-1/4 bg-gradient-to-r"></div>
                <div className="from-background pointer-events-none absolute inset-y-0 right-0 w-1/4 bg-gradient-to-l"></div>
            </div>
        </section>
    )
}
