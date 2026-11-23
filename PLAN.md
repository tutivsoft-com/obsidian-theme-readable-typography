# Readable Typography design plan

A typography-focused Obsidian theme for comfortable reading and writing.

This plan records the original design and scope from 13 November 2026. See the [README](README.md) for the implemented theme, compatibility, and installation instructions.

Search keywords: Obsidian theme, typography, readable text, line spacing, long-form reading.

## Who this is for

People who want clear text, visible bullets and generous spacing in long notes.

## User need and evidence

Users looking for readable setups discuss font choices, line spacing, faint bullets and the effort needed to customise a theme.

- [Fonts and long-session reading preferences](https://www.reddit.com/r/ObsidianMD/comments/1vfdfk7/themes_that_dont_hurt_the_eyes_to_read_through/)
- [Complaints about dim and tightly spaced bullets](https://www.reddit.com/r/ObsidianMD/comments/1vq2hww/what_theme_do_you_use/)

The Reddit links provide examples from the original research. Other themes and snippets may already address parts of these needs.

## Planned appearance and features

- Use generous line spacing, clear paragraph separation and a sensible reading width.
- Keep bullets visible and leave a clear gap between markers and text.
- Respect built-in font and font-size settings; avoid forcing tiny interface text.
- Consider optional Lexend or Atkinson Hyperlegible font guidance, with local installation or properly licensed offline assets.
- Provide optional controls for line length and spacing without making a settings plugin mandatory.
- Use clear heading hierarchy and link styling with balanced light and dark palettes.

## Mode scope

Plan both light and dark modes.

## Original implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references for later implementation:

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

## Original acceptance checklist

- [ ] Review long prose, lists, links and mixed scripts at different font sizes.
- [ ] Check font fallbacks and offline behaviour.
- [ ] Treat reading comfort as individual preference; do not promise dyslexia treatment, medical benefits or universal eye-strain relief.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Original planning scope

The original planning task covered repository creation and the design plan. Theme implementation followed in a later revision.
