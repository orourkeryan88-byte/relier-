import React from "react";
import { AbsoluteFill, Composition, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

const Test: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const pop = spring({ frame, fps, config: { damping: 12 } });
  const sweep = interpolate(frame, [0, 90], [0, 360]);
  return (
    <AbsoluteFill style={{ background: `linear-gradient(${sweep}deg, #0a1024, #1b2d5c)`, alignItems: "center", justifyContent: "center" }}>
      <div style={{ transform: `scale(${pop})`, color: "#3de3ff", fontSize: 140, fontWeight: 800, fontFamily: "sans-serif" }}>REMOTION OK</div>
      <div style={{ position: "absolute", bottom: 300, color: "#eaf2ff", fontSize: 56, fontFamily: "sans-serif" }}>frame {frame}</div>
    </AbsoluteFill>
  );
};

export const Root: React.FC = () => (
  <Composition id="Test" component={Test} durationInFrames={90} fps={30} width={1080} height={1920} />
);
