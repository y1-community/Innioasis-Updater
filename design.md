# Innioasis Lumen

A shared Hallmark design system for the Innioasis Updater site and its firmware documentation.

## Intent

Help a person safely install, update, or restore an Innioasis Y1 or Y2 without assuming they know what a ROM, scatter file, bootloader, or MediaTek tool is. The interface should feel calm, technical, and human. It should make the safe next action obvious.

## Visual DNA

- **Theme:** Lumen
- **Genre:** modern-minimal with an editorial documentation voice
- **Surface:** deep ink background with quiet blue light and warm amber warnings
- **Display type:** Instrument Serif, upright only
- **Body type:** DM Sans, with system fallbacks
- **Shape:** restrained radii, thin borders, no glassmorphism, no fake browser or app chrome
- **Motion:** short opacity and transform transitions only; no auto-advancing content
- **Iconography:** text labels first; icons are supplementary and never the only signal

## Voice

Use the words people see in Updater: **Device Type**, **Device Model**, **Software**, **Install / Restore**, **Install from .zip**, **Power off**, and **Connect the USB cable**.

Prefer:

- “Choose the model printed on your player.”
- “Updater downloads the matching package.”
- “Leave the cable connected until the app says you are finished.”
- “If the player does not start, install Original Software for the same model.”

Avoid:

- unexplained jargon
- fake certainty about a build or device state
- “seamless”, “effortless”, “revolutionary”, “unlock your potential”, and similar filler
- em-dash-heavy or breathless copy
- invented download counts, success rates, or safety claims

## Content model

Every guide permutation should state:

1. supported model and device type assumptions
2. what the project changes and what it does not
3. supplies and preparation
4. exact Updater labels in order
5. the power-off and USB connection moment
6. what success looks like
7. the restore path using Original Software
8. a project source link and a troubleshooting link

Screenshots are reused only when the UI state is genuinely the same. Stable filenames use `updater-<model>-<state>.png`.

## Accessibility contract

- one `h1` per page and a logical heading hierarchy
- every control has an accessible name
- visible `:focus-visible` rings
- no essential information conveyed by colour alone
- carousel controls work with keyboard and do not auto-advance
- YouTube iframes load only after activation and sit inside a fixed aspect-ratio box
- images declare intrinsic dimensions or use an aspect ratio
- reduced motion removes spatial transitions
- touch targets are at least 44px tall
- no horizontal overflow at 320, 375, 414, or 768px

## Performance contract

- static content is the first paint
- release refresh is non-blocking and unauthenticated in the browser; exact release assets stay on project release pages until a checked-in catalogue is deliberately generated
- no public GitHub token in HTML or JavaScript
- no third-party video iframe before the visitor asks for it
- no late content inserted above the current viewport
- stable screenshot dimensions and `decoding="async"`
- prefer one small shared stylesheet and one small shared interaction script

## Donation and feedback

Donation is optional, explicit, and never blocks installation. A useful guide may ask “Was this useful?” and reveal a quiet support link after a positive response. Feedback is stored locally unless a future server-backed system is explicitly added. No hidden donation prompts, fake urgency, preselected recurring gifts, or automatic popups.

## Hallmark pre-emit critique

- Philosophy: 5/5
- Hierarchy: 5/5
- Execution: 4/5
- Specificity: 5/5
- Restraint: 5/5
- Variety: 4/5
